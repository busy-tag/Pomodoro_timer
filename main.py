import signal
import threading
from setup_operations import handle_user_inputs, setup_directories, config_setup
from serial_operations import open_serial_connection, find_busy_tag_device
from timer_operations import run_session, cleanup
from image_operations import generate_last_10_images

stop_event = threading.Event()

def signal_handler(sig, frame):
    print("Ctrl+C detected! Stopping...")
    stop_event.set()

def main():
    signal.signal(signal.SIGINT, signal_handler)

    drive_letter, countdown_time_sec, break_time_sec = handle_user_inputs()
    output_dir, font_path, config_file = setup_directories(drive_letter)
    config_setup(config_file)

    print("Setup in progress\nPlease wait...")
    generated_files = generate_last_10_images(font_path, output_dir, countdown_time_sec, "countdown")
    generated_files += generate_last_10_images(font_path, output_dir, break_time_sec, "break")
    print("Loading assets completed")

    ser = open_serial_connection(find_busy_tag_device())
    if ser is None:
        return

    try:
        run_session(ser, countdown_time_sec, font_path, output_dir, "countdown", stop_event)
        print("Work session ended. Starting break...")
        run_session(ser, break_time_sec, font_path, output_dir, "break", stop_event)
    finally:
        generated_files.append(f"{output_dir}://countdown.png")
        cleanup(ser, generated_files)

if __name__ == "__main__":
    main()