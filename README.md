# PassURLs

<p align="center">
    <img src="https://github.com/user-attachments/assets/fbfcf508-0cdd-4383-bf48-72ce787cb18f" alt="subExtreme Screenshot" width="80%"/>
</p>


**PassURLs** is a simple and easy-to-use tool designed to pass a list of URLs from a text file through a proxy. This allows you to route the requests through tools like Burp Suite or any other proxy configured on a specific port, enabling you to capture all the requests made by the tool. The tool uses threading to speed up the process and provides color-coded feedback using the `colorama` library. Developed by [Ahmed Hamdy](https://github.com/ahmedhamdy0x) from [Gentil Security](https://www.youtube.com/@gentil.security).

## Features
- Pass URLs through a proxy, allowing tools like Burp Suite to capture requests.
- Use multiple threads to speed up the URL checking process.
- Color-coded output for easy visual feedback using the `colorama` library.
- Simple, user-friendly design for quick use.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ahmedhamdy0x/passurls.git
```

### 2. Create a virtual environment

To install the tool in an isolated environment, first create a virtual environment:

```bash
python -m venv passurls-env
```

### 3. Activate the virtual environment

To activate the virtual environment:

```bash
source passurls-env/bin/activate
```

### 4. Install the tool

Once the virtual environment is activated, install the tool and its dependencies:

```bash
cd passurls
pip install .
pip install -r requirements.txt
```

### 5. Install the tool globally

To use the tool from anywhere without activating the virtual environment each time, copy the executable script to a system-wide directory:

```bash
sudo cp ~/passurls-env/bin/passurls /usr/local/bin/
```

### 6. Deactivate the virtual environment

After installing, you can deactivate the virtual environment:

```bash
deactivate
cd ../
```

## Usage

You can now use the tool from anywhere on your system by simply typing:

```bash
passurls -h
```

To display the help and usage instructions.

### Basic example:

```bash
passurls -p 127.0.0.1:8080 -l /path/to/urls.txt -t 10
```

### Arguments:

- `-p` or `--proxy`: The proxy address (e.g., `127.0.0.1:8080`). This is where Burp Suite or any proxy tool is running, so it can capture the requests.
- `-l` or `--list`: Path to a file containing the list of URLs to pass through the proxy (e.g., `/path/to/urls.txt`).
- `-t` or `--threads`: Number of threads to use for sending requests (default is 10).

### Another example:

```bash
passurls -p 127.0.0.1:8080 -l urls.txt -t 20
```

This command will send all the URLs listed in `urls.txt` through the proxy (e.g., Burp Suite running on `127.0.0.1:8080`) and capture the requests.

## License

This project is licensed under the **GPL-3.0 License**. See the [LICENSE](LICENSE) file for details.

## Contact

- [Ahmed Hamdy](https://facebook.com/ahmedhamdy0x)
- Twitter: [@ahmedhamdy0x](https://twitter.com/ahmedhamdy0x)
- Youtube: [Gentil Security](https://www.youtube.com/@gentil.security)
- Email: info.gentil.academy@gmail.com

