---
title: "Hardmod Downgrade"
permalink: /hardmod-downgrade.html
---

The version of autofirm used in this guide was modified from [Reboot.ms](https://www.reboot.ms/forum/threads/2403/)'s autofirm which was modified from '[Raugo](https://gbatemp.net/members/356694/)'s original autofirm ([with permission](http://archive.is/KOrWp)).
{: .notice}  

An excellent guide to getting a hardmod can be found [here](https://gbatemp.net/threads/414498/).
{: .notice--info}

This is a currently working implementation of the "FIRM partitions known-plaintext" exploit detailed [here](https://www.3dbrew.org/wiki/3DS_System_Flaws).
{: .notice--info}

This will work on New 3DS, Old 3DS, and 2DS.
{: .notice--success}

#### What you need

* Your NAND image extracted using your [hardmod](https://gbatemp.net/threads/414498/)
* The latest version of [autofirm](https://github.com/Plailect/autofirm/archive/master.zip)
* The latest release of [3DSident](https://github.com/joel16/3DSident/releases/latest)
* The firmware zip corresponding to your device and version:
    + <a href="https://plailect.github.io/Guide/torrents/11.0.0_to_10.4.0_n3ds.torrent" target="_blank">New 3DS 11.0.0 to 10.4.0</a>
    + <a href="https://plailect.github.io/Guide/torrents/11.0.0_to_10.4.0_o3ds.torrent" target="_blank">Old 3DS or 2DS 11.0.0 to 10.4.0</a>     
    ~    
    + <a href="https://plailect.github.io/Guide/torrents/11.1.0_to_10.4.0_n3ds.torrent" target="_blank">New 3DS 11.1.0 to 10.4.0</a>     
    + <a href="https://plailect.github.io/Guide/torrents/11.1.0_to_10.4.0_o3ds.torrent" target="_blank">Old 3DS or 2DS 11.1.0 to 10.4.0</a>     
    ~    
    + <a href="https://plailect.github.io/Guide/torrents/11.2.0_to_10.4.0_n3ds.torrent" target="_blank">New 3DS 11.2.0 to 10.4.0</a>     
    + <a href="https://plailect.github.io/Guide/torrents/11.2.0_to_10.4.0_o3ds.torrent" target="_blank">Old 3DS 11.2.0 to 10.4.0</a>    

#### Instructions_

##### Section I - NAND modification

1. Extract the autofirm zip to a folder called `autofirm`
2. Place a copy of your NAND backup (named `nand.bin`) in `/autofirm/` folder
3. Copy the contents of the firmware zip to the `/autofirm/source/firmwares/` folder
4. Run `autofirm.bat` and select which device and version the NAND backup is for
5. Wait while the script runs
6. If everything worked, then your original NAND will have been renamed to `backup_nand.bin` and you will have a modified `nand.bin` containing the 10.4.0 NATIVE_FIRM
7. Flash this `nand.bin` to your device with your hardmod

##### Section II - Exploit verification

1. Copy and merge the `3ds` folder from the 3DSident zip to your device's SD card
2. Reinsert your SD card into your 3DS
3. Use [Homebrew Launcher (No Browser)](homebrew-launcher-(no-browser)) to launch the homebrew launcher on the device
4. Launch 3DSident
5. Verify that the following:
  + **Kernel version**: 2.50-11
  + **FIRM version**: 2.50-11
  + If either of these do not display the versions above, something has gone wrong and you should try again from the beginning

Your version number will *not* have changed in the settings.
{: .notice--info}

Continue to [Homebrew Launcher (No Browser)](homebrew-launcher-(no-browser)).
{: .notice--primary}
