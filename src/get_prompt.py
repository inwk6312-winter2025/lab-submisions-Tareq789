
m netmiko import Netmiko

# Define your devices
devices = [
            {
                        "device_type": "cisco_ios",
                                "ip": "192.168.1.101",  # Router 1
                                        "username": "student",
                                                "password": "Meilab123",
                                                        "secret": "cisco",
                                                                "port": "22",
                                                                    },
                {
                            "device_type": "cisco_ios",
                                    "ip": "192.168.1.102",  # Router 2
                                            "username": "student",
                                                    "password": "Meilab123",
                                                            "secret": "cisco",
                                                                    "port": "22",
                                                                        },
                    {
                                "device_type": "cisco_ios",
                                        "ip": "192.168.1.103",  # Router 3
                                                "username": "student",
                                                        "password": "Meilab123",
                                                                "secret": "cisco",
                                                                        "port": "22",
                                                                            }
                    ]

# Loop through each device in the devices list
for device in devices:
        try:
                    # Establish the connection to the device
                            net_connect = Netmiko(**device)

                                    # Print the default prompt
                                            print(f"Connecting to {device['ip']}...")
                                                    print(f"Default prompt for {device['ip']}: {net_connect.find_prompt()}")

                                                            # Issue the disable command
                                                                    net_connect.send_command_timing("disable")
                                                                            print(f"Disable command for {device['ip']}: {net_connect.find_prompt()}")

                                                                                    # Issue the enable command again
                                                                                            net_connect.enable()
                                                                                                    print(f"Enable command for {device['ip']}: {net_connect.find_prompt()}")
                                                                                                            
                                                                                                                    # Close the connection
                                                                                                                            net_connect.disconnect()
                                                                                                                                    
                                                                                                                                        except Exception as e:
                                                                                                                                                    print(f"Failed to connect to {device['ip']}: {str(e)}"
