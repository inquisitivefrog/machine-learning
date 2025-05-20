(JupyterSystemEnv) sh-4.2$ cat inspect_hardware.sh 
#!/bin/bash
echo "Instance Type:"
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-type
echo -e "\nCPU Info:"
lscpu
echo -e "\nMemory Info:"
free -h
echo -e "\nDisk Info:"
df -h
echo -e "\nGPU Check:"
lspci | grep -i nvidia || echo "No NVIDIA GPU detected"
nvidia-smi || echo "nvidia-smi not available"
