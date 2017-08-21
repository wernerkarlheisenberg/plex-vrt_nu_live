# plex-vrt_nu_live
Plex Plugin to view VRT channels (één, canvas, ketnet) live using VRT_NU.

# Installation Instructions
The installation does not require additional steps compared with the installation of other plugins.
1. Download a copy of the repository as ZIP file and unzip.
2. Download a copy of [requests](https://github.com/requests/requests) and unzip it under 'VRT_NU_live.bundle/Contents/Libraries/requests'.
3. Copy VRT_NU_live.bundle to the Plex Plugin folder.
4. To be on the safe side, restart the Plex Server.
5. Click the "Channels" menu item in Plex.

# VRT_NU Archive
This plugin is meant to livestream VRT channels using VRT NU. VRT NU also contains an
archive, which is not accessible via this plugin. If there is interest to access this
archive via a Plex Plugin and want to collaborate, please let me know.

# Known Issues
* People using Windows 8(.1), please have a look at [Issue 3](https://github.com/wernerkarlheisenberg/plex-stieve/issues/3). It turns out that the included python libraries in Plex Media Server differ between platforms.

# Issues
When have problems, please file an issue. To speed up the troubleshooting process, please add a copy of the plugin (com.plexapp.plugins.vrt_nu.log), system (com.plexapp.system.log) and server log (Plex Media Server.log).
