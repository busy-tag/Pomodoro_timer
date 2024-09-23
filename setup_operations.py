import json  

def read_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()

        try:
            config = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON config file: {e}")
            return None
        
    return config

def update_config(section, option, value, config_file):
    config = read_config(config_file)
    if config is None:
        return

    if section not in config:
        config[section] = {}

    config[section][option] = value

    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

def input_or_default(prompt, default):
    user_input = input(f"{prompt} or press Enter for default {default}min: ").strip()
    return int(user_input) if user_input.isdigit() else default

def handle_user_inputs():
    drive_letter = input("Enter the Busy Tag disk drive letter (e.g., D or E): ").strip().upper()
    drive_letter = drive_letter if len(drive_letter) == 1 and drive_letter.isalpha() else 'D'
    countdown_time_min = input_or_default("Enter the countdown time in minutes", 25)
    break_time_min = input_or_default("Enter the break time in minutes", 5)
    return drive_letter, countdown_time_min * 60, break_time_min * 60

def setup_directories(drive_letter):
    output_dir = f"{drive_letter}"
    font_path = "MontserratBlack-3zOvZ.ttf"
    config_file = f"{output_dir}://config.json"
    return output_dir, font_path, config_file

def config_setup(config_file):
    config = read_config(config_file)
    if config:
        update_config('settings', 'show_after_drop', False, config_file=config_file)
        update_config('settings', 'activate_pattern', False, config_file=config_file)