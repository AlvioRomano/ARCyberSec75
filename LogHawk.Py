# loghawk.py

import re
import argparse
import yaml
import os
import datetime
import subprocess

# Load regex patterns from YAML config file

def load_patterns(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config.get('patterns', []), config.get('log_paths', []), config.get('alert_log', 'alerts.log')

# Search logs using regex (Python re module)

def search_logs_with_regex(log_paths, patterns):
    alerts = []
    for path in log_paths:
        if not os.path.isfile(path):
            continue
        with open(path, 'r', errors='ignore') as f:
            for line in f:
                for pattern in patterns:
                    if re.search(pattern, line):
                        alerts.append((path, line.strip(), pattern))
    return alerts

# Alternative: Search logs using grep (optional)

def search_logs_with_grep(log_paths, patterns):
    alerts = []
    for path in log_paths:
        if not os.path.isfile(path):
            continue
        for pattern in patterns:
            try:
                result = subprocess.run(['grep', '-E', pattern, path], capture_output=True, text=True)
                if result.stdout:
                    for line in result.stdout.strip().split('\n'):
                        alerts.append((path, line.strip(), pattern))
            except Exception as e:
                print(f"Error using grep on {path}: {e}")
    return alerts

# Write alerts to log file

def write_alerts(alerts, alert_log):
    with open(alert_log, 'a') as f:
        for path, line, pattern in alerts:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[{timestamp}] ALERT in {path}: Matched '{pattern}' => {line}\n")
            print(f"[!] Alert: {line} (Matched: {pattern})")

# Main logic

def main():
    parser = argparse.ArgumentParser(description='LogHawk - Log Monitoring Tool')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to config YAML file')
    parser.add_argument('--use-grep', action='store_true', help='Use grep instead of Python regex')
    args = parser.parse_args()

    patterns, log_paths, alert_log = load_patterns(args.config)

    if args.use_grep:
        alerts = search_logs_with_grep(log_paths, patterns)
    else:
        alerts = search_logs_with_regex(log_paths, patterns)

    if alerts:
        write_alerts(alerts, alert_log)
    else:
        print("No alerts found.")

if __name__ == '__main__':
    main()
