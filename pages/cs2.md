---
tags:
- linkup
title: CS2
---

# CS2

Setting up a CS2 server on Linux

## Assumptions

This guide assumes that you will use `/home/steam/games` as `$CS2_ROOT` and argument to `force_install_dir`

## Prerequisites

- Clone the CS2 repository
    - `git clone https://github.com/jakestanley/cs2.git`

## Set up Steam

- Create `steam` user with home directory
    - `sudo useradd -m steam`
- Switch to the `steam` user and their home directory
    - `sudo su steam`
    - `cd`
- Set up SteamCMD
    - `steamcmd`
    - `Steam> force_install_dir /home/steam/games`
    - `Steam> login <steam_username>`
        - This step requires entering Steam Guard code first
- Install CS2
    - `Steam> app_update 730 validate`
- Exit SteamCMD safely
    - `Steam> quit`
- Link Steam client shared object
    - `mkdir -p $HOME/.steam/sdk64`
    - `ln -s $HOME/.local/share/Steam/steamcmd/linux64/steamclient.so $HOME/.steam/sdk64/`
- You can update later with a one-liner
    - `steamcmd +force_install_dir $HOME/games +login <steam_username> +app_update 730 validate +quit`

## Configure CS2 server

- Generate a [Steam game server token](https://steamcommunity.com/dev/managegameservers)
- Populate `$CS2_ROOT/csgo/cfg/server.cfg` with the following lines:
    - `sv_setsteamaccount <steam-game-server-token>`
    - `rcon_password <super-secure-password>`

## Configure power options

On Ubuntu 22.04 LTS, the `powersave` governor is enabled by default. You may wish to switch to the `performance` governer to reduce slow server frame warnings:

- Install cpufrequtils
    - `sudo apt update && sudo apt install cpufrequtils`
- Switch to performance with 
    - `sudo cpufreq-set -r -g performance`
- Switch back to powersave with 
    - `sudo cpufreq-set -r -g powersave`

## Start the server 

- Switch to the CS2 repository
- `cd cs2`
- `./cs2.sh`

## Control maps and game modes for a running server

- Check out the CS2 repository on a computer you have desktop access to
- Install Python dependencies
    - `pip install -r requirements.txt`
- Run the controller
    - `python control.py -H <server-address>`

## Set up CS2 server mods (optional)

- From the CS2 repository, install server mods if you wish with the `install_server_mods.sh` script
    - Note that you may need to update the URLs in the script to latest releases
    - Currently only deathmatch mod is installed by the script
- Ensure that $HOME/games/game/csgo/gameinfo.gi has the line
    - Game    csgo/addons/metamod
    - directly underneath
    - Game_LowViolence    csgo_lv
- If this is set up correctly, the server command 'meta list' should work

### Configure deathmatch mod