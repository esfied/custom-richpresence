# custom-richpresence
Personal Discord activity status for apps that doesn't support Rich Presence / Lacks image. (Mac & Linux)

<img width="307" alt="Screen Shot 2023-06-19 at 10 47 41 PM" src="https://github.com/esfied/custom-richpresence/assets/136987425/fddaf205-199c-490b-8e9c-3848cdd3c07b">

## Attribution
The `rpc.py` file used in this project is obtained from the [niveshbirangal/discord-rpc](https://github.com/niveshbirangal/discord-rpc) repository.

## Set-up
1. Go to https://discord.com/developers/applications.

2. Create your "New Application" for the activity you want to appear on your profile.

3. Choose a "NAME" for the application, and copy the "APPLICATION ID".

4. Then go to the "Rich Presence" tab and add an image you want for the icon by clicking "Add Image(s)" in the "Rich Presence Assets". (512x512 is the minimum)

## Usage (Mac)
5. Ensure that you have Python 3.x installed on your system.

6. Clone this repository to your local machine (Recommended to be on your home folder, /Users/yourname).

7. Edit `richpresence.py` and `start_rich_presence.sh` to add the application's client ID and the extra details. Refer to the comments in the code.

8. To automatically run at startup, go to System Preferences > Users & Groups > Login Items, and add `start_rich_presence.sh`, then restart your device.

9. Feel free to start Discord and see your activity by starting your chosen executable :)
