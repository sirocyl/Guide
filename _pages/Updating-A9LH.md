---
title: "Updating A9LH"
permalink: /updating-a9lh.html
---

The actual installation of arm9loaderhax itself consists of payload files installed into the firmware partitions on your device's NAND chip, which is soldered to the motherboard itself. These payloads are updated rarely and only really serve the purpose of launching `arm9loaderhax.bin` from the SD Card, which is, in our case, Luma3DS.
{: .notice}

So far, arm9loaderhax itself has only been majorly updated once.
{: .notice--info}

The old version of arm9loaderhax (sometimes referred to as "v1" because it was installed using SafeA9LHInstaller v1) was the latest version of [Delebile's initial implementation](https://github.com/delebile/arm9loaderhax).
{: .notice--info}

The new version of arm9loaderhax (sometimes referred to as "v2" because it is installed using SafeA9LHInstaller v2 or FIRM81 because of its use of 8.1's firmware files to make room for larger payloads) is the latest version of [AuroraWright's Fork](https://github.com/AuroraWright/arm9loaderhax) of [Delebile's initial implementation](https://github.com/delebile/arm9loaderhax).
{: .notice--info}

These steps will also update your various payloads and the AES key database.
{: .notice--success}

#### What you need

* <a href="https://plailect.github.io/Guide/torrents/aeskeydb.torrent" target="_blank">`aeskeydb.bin`</a>
* <a href="https://plailect.github.io/Guide/torrents/data_input_v3.torrent" target="_blank">`data_input_v3.zip`</a>
* The latest release of [arm9loaderhax](https://github.com/AuroraWright/arm9loaderhax/releases/latest)
* The latest release of [SafeA9LHInstaller](https://github.com/AuroraWright/SafeA9LHInstaller/releases/latest)
* The latest release of [Hourglass9](https://github.com/d0k3/Hourglass9/releases/latest)

#### Instructions

**For all of these instructions, OVERWRITE any existing files on your SD card.**

1. Delete any existing `aeskeydb.bin` from the root of your SD card
4. Delete the `a9lh` folder from the root of your SD card if it exists
2. Copy `aeskeydb.bin` to the `/files9/` folder on your SD card
3. Copy `Hourglass9.bin` from the Hourglass9 zip to the `/luma/payloads/` folder on your SD card and rename `Hourglass9.bin` to `start_Hourglass9.bin`
5. Copy `arm9loaderhax.bin` from the SafeA9LHInstaller zip to the `/luma/payloads` folder on your SD card
6. Rename `arm9loaderhax.bin` in `/luma/payloads` to `down_safea9lhinstaller.bin`
7. Copy the `a9lh` folder from `data_input_v3.zip` to the root of your SD Card
7. Copy _the contents of_ the arm9loaderhax zip to `a9lh` folder on your SD card
9. Reinsert your SD card into your 3DS
10. Boot the device while holding D-Pad down
11. Press (Select) to update arm9loaderhax
12. Power off the device and put your SD card back in your computer
13. Delete the `a9lh` folder from the root of your SD card
14. Delete `down_safea9lhinstaller.bin` from `/luma/payloads`
15. Reinsert your SD card into your 3DS and boot
