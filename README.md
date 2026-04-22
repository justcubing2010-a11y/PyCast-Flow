# PyCast-Flow
Stream your videos to your tv without any lag

# PyCast-Flow 🎥

A robust, zero-dependency Python media server designed to stream video files from a mobile device (Pydroid 3) to a Smart TV.

## The Problem
Standard Python servers (`http.server`) often crash with `BrokenPipeError` or `ConnectionResetError` when used with TVs. This is because TVs attempt to "seek" or "buffer" by requesting specific byte ranges, which the default server doesn't support.

## The Solution
**PyCast-Flow** implements a custom request handler that:
- ✅ **Supports Byte-Range Requests**: Smooth seeking and buffering.
- ✅ **Multi-threaded**: Handles simultaneous connections without hanging.
- ✅ **Zero Setup**: Just drop the script in your movie folder and run.

## Usage
1. Open **Pydroid 3** on your Android device.
2. Move `main.py` into your movies directory.
3. Run the script.
4. On your TV, enter your phone's IP: `http://192.168.x.x:8000`.

## License
MIT
