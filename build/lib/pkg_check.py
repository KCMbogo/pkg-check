import argparse
import importlib.metadata
import subprocess

def main():
    parser = argparse.ArgumentParser(prog="pkg-check", description="A tool that checks if a package is installed")
    parser.add_argument("package")

    args = parser.parse_args()
    # print("Package:", args.package)

    package_name = args.package

    try:
        version = importlib.metadata.version(package_name)
        print(f"Package: {package_name} is installed (version: {version})")
    except importlib.metadata.PackageNotFoundError:
        print(f"Package: {package_name} is not installed")
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
                        print("No dependencies")
                    else:
                        print("Dependencies")
                        for dep in deps.split(","):
                            print("-", dep.strip())
                    return
            print("No dependencies info found")

        except subprocess.CalledProcessError as e:
            print("Failed to fetch dependency info:", e)
        
    get_dependencies(package_name)

if __name__ == "__main__":
    main()