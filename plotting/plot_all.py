import subprocess
for s in ["fig5a.py","fig5b.py","fig5c.py","fig6a.py","fig6b.py","fig6c.py","fig7a.py","fig7b.py","fig7c.py"]:
    subprocess.check_call(["python",f"plotting/{s}"])
print("ok")
