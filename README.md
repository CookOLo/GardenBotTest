# GardenBotTest

**Note:** _Contact me for key_

## Purpose
To test the Wi-Fi connection at the West Valley Gardens using a Discord Bot.

Sees if:
- The Garden can handle sending very small packages (numbers) over the Wi-Fi from a device (wherever you execute the code) to some server (Discord's servers in this case)
- Over Wi-Fi, small packages can be sent to a device near the gardens (sent to the server that'll we'll see from a device at the Gardens)

Why?
- To test if a moisture sensor sending packets over Wi-Fi is feasable

## Description
Simple script that:
- Starts when "count @garden test" is sent in a Discord channel
- Bot will count down from 30 to 0 every minute, sending in "00:XX" format from the same channel the starter message was sent

