import os
import time
from image_operations import create_text_to_image
from serial_operations import send_serial_command, close_serial_connection
from image_operations import delete_generated_files

def handle_last_10_seconds(ser, stop_event, countdown_type="countdown"):
    countdown_time_sec = 9
    while countdown_time_sec >= 0 and not stop_event.is_set():
        minutes, seconds = divmod(countdown_time_sec, 60)
        countdown_display = f"{minutes:02d}_{seconds:02d}"
        file_name = f"countdown_{countdown_display}.png"
        send_serial_command(ser, f'AT+SP={file_name}')

        countdown_time_sec -= 1
        time.sleep(1)
        if stop_event.is_set():
            break
    time.sleep(1)
    send_serial_command(ser, 'AT+PP=1,0')

def generate_and_send_images(session_time_sec, font_path, output_dir, ser, stop_event, session_type):
    minutes, seconds = divmod(session_time_sec, 60)
    countdown_display = f"{minutes:02d}:{seconds:02d}"

    start_time = time.time()
    last_command_time = start_time
    total_intervals = session_time_sec / 5
    one_cycle_fill = 360 / total_intervals
    fill_amount = 0
    print(f"{session_type.capitalize()} started...")

    while session_time_sec >= 10 and not stop_event.is_set():
        minutes, seconds = divmod(session_time_sec, 60)
        countdown_display = f"{minutes:02d}:{seconds:02d}"
        file_name = "countdown.png"
        output_file = f"{output_dir}://{file_name}"
        create_text_to_image(width=240, height=280, countdown_time=countdown_display, font_path=font_path, output_file=output_file, fill_amount=fill_amount)
        
        while True:
            current_time = time.time()
            if current_time - last_command_time >= 5:
                send_serial_command(ser, f'AT+SP=countdown.png')
                last_command_time = current_time
                break
            time.sleep(0.1)
        
        fill_amount += one_cycle_fill
        session_time_sec -= 5
        time.sleep(0.5)
    
    handle_last_10_seconds(ser, stop_event, session_type)

def run_session(ser, session_time_sec, font_path, output_dir, session_type,stop_event):
    send_serial_command(ser, f"AT+SC={'127,990000' if session_type == 'countdown' else '127,00FF00'}")
    time.sleep(2)
    generate_and_send_images(session_time_sec, font_path, output_dir, ser, stop_event, session_type)

def cleanup(ser, generated_files):
    delete_generated_files(generated_files)
    close_serial_connection(ser)