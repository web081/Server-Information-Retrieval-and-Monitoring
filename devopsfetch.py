#!/usr/bin/env python3

import sys
import subprocess
from datetime import datetime
from tabulate import tabulate
import json

def list_ports():
    result = subprocess.run(['netstat', '-tuln'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def port_details(port_number):
    result = subprocess.run(['netstat', '-anp'], stdout=subprocess.PIPE)
    details = [line for line in result.stdout.decode('utf-8').split('\n') if f':{port_number}' in line]
    return details

def list_docker_images():
    result = subprocess.run(['docker', 'images'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def list_docker_containers():
    result = subprocess.run(['docker', 'ps', '-a'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def docker_container_details(container_name):
    result = subprocess.run(['docker', 'inspect', container_name], stdout=subprocess.PIPE)
    return json.loads(result.stdout)

def list_nginx_domains():
    result = subprocess.run(['nginx', '-T'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def nginx_domain_details(domain):
    config_path = f'/etc/nginx/sites-available/{domain}'
    with open(config_path, 'r') as file:
        return file.readlines()

def list_users():
    result = subprocess.run(['lastlog'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def user_details(username):
    result = subprocess.run(['finger', username], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def filter_logs_by_time(logs, start_time, end_time):
    filtered_logs = []
    for log in logs.split('\n'):
        log_time_str = log.split()[0]
        log_time = datetime.strptime(log_time_str, '%b %d %H:%M:%S')
        if start_time <= log_time <= end_time:
            filtered_logs.append(log)
    return filtered_logs

def format_table(data, headers):
    return tabulate(data, headers=headers, tablefmt='grid')

def print_help():
    print("""
Usage: devopsfetch [options]

Options:
  --port <port_number>       Show details for a specific port.
  --docker <container_name>  Show details for a specific Docker container.
  --nginx <domain>           Show configuration for a specific Nginx domain.
  --users                    List all users and their last login.
  --time <start_time> <end_time>  Filter logs by time range.
  -h, --help                 Show this help message and exit.
""")

def main():
    if '--port' in sys.argv:
        if len(sys.argv) == 3:
            port_number = sys.argv[2]
            details = port_details(port_number)
            print(format_table(details, headers=['Port Details']))
        else:
            print("Usage: devopsfetch --port <port_number>")
    elif '--docker' in sys.argv:
        if len(sys.argv) == 3:
            container_name = sys.argv[2]
            details = docker_container_details(container_name)
            print(format_table(details, headers=['Container Details']))
        else:
            print("Usage: devopsfetch --docker <container_name>")
    elif '--nginx' in sys.argv:
        if len(sys.argv) == 3:
            domain = sys.argv[2]
            details = nginx_domain_details(domain)
            print(format_table(details, headers=['Nginx Domain Details']))
        else:
            print("Usage: devopsfetch --nginx <domain>")
    elif '--users' in sys.argv:
        if len(sys.argv) == 2:
            users = list_users()
            print(format_table(users, headers=['Users and Last Login']))
        else:
            print("Usage: devopsfetch --users")
    elif '--time' in sys.argv:
        if len(sys.argv) == 4:
            start_time = datetime.strptime(sys.argv[2], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(sys.argv[3], '%Y-%m-%d %H:%M:%S')
            logs = subprocess.run(['journalctl'], stdout=subprocess.PIPE).stdout.decode('utf-8')
            filtered_logs = filter_logs_by_time(logs, start_time, end_time)
            print(format_table(filtered_logs, headers=['Logs in Time Range']))
        else:
            print("Usage: devopsfetch --time <start_time> <end_time>")
    else:
        print_help()

if __name__ == "__main__":
    main()
