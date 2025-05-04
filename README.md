# Transmission Builds

This repository contains automated build scripts for compiling the Transmission BitTorrent client and creating Debian packages (.deb). The builds are automated via GitHub Actions and support multiple Linux distributions.

## Features

- Automated builds via GitHub Actions
- Debian packages that install Transmission in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}`
- Support for multiple Linux distributions:
  - Debian 11 (Bullseye)
  - Debian 12 (Bookworm)
  - Ubuntu 22.04 LTS
  - Ubuntu 24.04 LTS
- Multiple version support with different stability levels:
  - Stable (4.0.6)
  - Oldstable (4.0.3, 4.0.4, 4.0.5)
  - Next (4.1.0-beta.2)
- Static compilation for server usage
- Web interface support
- JSON-RPC API support
- Automated metadata generation
- Package signing and verification

## Build Process

The build process is fully automated and includes:
1. Environment setup with all required dependencies
2. Download and compilation of Transmission
3. Static linking of all components
4. Creation of Debian packages
5. Generation of JSON metadata
6. Package signing and verification
7. Automated release creation

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs Transmission in a dedicated directory structure:
- Base installation path: `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}`
- Binaries in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}/usr/bin`
- Libraries in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}/usr/lib`
- Web interface in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}/usr/share/transmission/web`
- Documentation in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}/usr/share/doc/transmission`
- Systemd service file in `/opt/MediaEase/.binaries/installed/transmission-${STABILITY}_${VERSION}/usr/lib/systemd/system`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

### Build Configuration
The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for different versions and distributions

## License

This repository is licensed under the terms specified in the LICENSE file.

Transmission is distributed under the terms of the [GNU General Public License v2](https://www.gnu.org/licenses/gpl-2.0.html) or later.
