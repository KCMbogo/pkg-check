import argparse
import importlib.metadata
import subprocess
import requests
import socket
import difflib

def is_package_on_pypi(package_name: str) -> bool:
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    return response.status_code == 200

def has_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False
    
def suggest_similar_package(package_name: str, max_suggestions: int=3):
    response = requests.get("https://pypi.org/simple/")
    if response.status_code != 200:
        return []
    
    package_list = response.text.splitlines()
    matches = difflib.get_close_matches(package_name.lower(), package_list, n=max_suggestions, cutoff=0.6)
    return matches

def install_package(package_name: str):
    try:
        result = subprocess.run(
            ["pip", "install", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ Installed '{package_name}':\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing '{package_name}':\n{e.stderr}")

def main():
    parser = argparse.ArgumentParser(prog="pkg-check", description="A tool that checks if a package is installed")
    parser.add_argument("package")

    args = parser.parse_args()
    package_name = args.package

    try:
        version = importlib.metadata.version(package_name)
        print(f"✅ {package_name} is installed (version: {version})")
    except importlib.metadata.PackageNotFoundError:
        print(f"❌ {package_name} is not installed")
        if has_internet():
            if is_package_on_pypi(package_name=package_name):
                response = input("Would you like to install the package?N/y?")
                if response == "y" or response == "Y":
                    install_package(package_name)
                elif response == "N" or response == "n":
                    print(f"Ok...!")
                    exit()
                else:
                    pass    
            else:
                suggestions = suggest_similar_package(package_name)
                if suggestions:
                    print(f"😇 Did you mean one of these packages:")
                    for s in suggestions:
                        print(f" - {s}")
                else:
                    print(f"😓 I couldn't find it on PyPI either")
        exit(1)

    def get_dependencies(package):
        try: 
            result = subprocess.run(
                ["pip", "show", package],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )

            # Extract "Requires: ..." line
            lines = result.stdout.splitlines()
            for line in lines:
                if line.startswith("Requires:"):
                    deps = line.replace("Requires:", "").strip()
                    if not deps:
                        print("📦 No dependencies")
                    else:
                        print("📦 Dependencies")
                        for dep in deps.split(","):
                            print("-", dep.strip())
                    return
            print("📦 No dependencies info found")

        except subprocess.CalledProcessError as e:
            print("❌ Failed to fetch dependency info:", e)
        
    get_dependencies(package_name)

if __name__ == "__main__":
    main()