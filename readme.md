# Radian Video Recorder

Radian Video Recorder is an embedded video recording and video streaming application developed by **Radiantech-Systems**.

The project is designed to capture video streams, record video footage, and provide video streaming functionality for embedded systems.

## Overview

The application consists of two main components:

- **Video Recorder** – Captures and records video streams to the local system.
- **Video Server** – Provides access to video streams for monitoring and playback.

The project uses **GStreamer** for video processing and is designed to run efficiently on ARM64-based embedded platforms.

## Features

- Real-time video recording
- Video streaming support
- GStreamer-based video processing
- Local video storage
- Video server functionality
- Automatic service-based execution
- ARM64 / AArch64 platform support
- Lightweight design for embedded systems

## Architecture

```text
             Video Source
                  │
                  ▼
        ┌──────────────────┐
        │  Video Recorder  │
        └────────┬─────────┘
                 │
                 ▼
          Video Recordings
                 │
                 │
                 ▼
        ┌──────────────────┐
        │   Video Server   │
        └────────┬─────────┘
                 │
                 ▼
        Monitoring / Client
```

## Components

### Video Recorder

The Video Recorder component is responsible for receiving video streams and storing recorded footage locally.

It is designed to operate continuously as a background service on the target embedded system.

### Video Server

The Video Server provides video streaming functionality, allowing recorded or live video content to be accessed by connected clients.

The server is implemented using Python and Flask-based components.

## Services

The application provides two system services:

- `video-recorder.service`
- `video-server.service`

These services allow the recorder and video server to run automatically as part of the embedded system.

## Project Structure

```text
asrock_video-recorder/
│
├── files/
│   ├── src/
│   ├── include/
│   ├── videoserver.py
│   ├── video-recorder.service
│   ├── video-server.service
│   └── ...
│
├── debian/
│
├── radian-video-recorder.bb
│
└── README.md
```
clone:
git clone https://github.com/Radiantech-Systems/asrock_video-recorder.git
for build purpose on ubuntu :
sudo apt update
sudo apt install -y build-essential debhelper devscripts
dpkg-buildpackage -us -uc -b


## Purpose

The main purpose of this project is to provide a reliable and lightweight video recording and streaming solution for **Radian embedded systems**.

It can be integrated into an embedded video monitoring system where video needs to be captured, stored, and accessed remotely.

## Organization

Developed and maintained by **Radiantech-Systems**.

**GitHub:**  
https://github.com/Radiantech-Systems
