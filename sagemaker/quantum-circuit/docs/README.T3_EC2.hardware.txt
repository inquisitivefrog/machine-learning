
sh-4.2$ lspci
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma]
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.3 Non-VGA unclassified device: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:03.0 VGA compatible controller: Amazon.com, Inc. Device 1111
00:04.0 Non-Volatile memory controller: Amazon.com, Inc. Device 8061
00:05.0 Ethernet controller: Amazon.com, Inc. Elastic Network Adapter (ENA)
00:06.0 Ethernet controller: Amazon.com, Inc. Elastic Network Adapter (ENA)
00:1f.0 Non-Volatile memory controller: Amazon.com, Inc. Device 8061

sh-4.2$ lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              2
On-line CPU(s) list: 0,1
Thread(s) per core:  2
Core(s) per socket:  1
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               85
Model name:          Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz
Stepping:            7
CPU MHz:             2500.004
BogoMIPS:            5000.00
Hypervisor vendor:   KVM
Virtualization type: full
L1d cache:           32K
L1i cache:           32K
L2 cache:            1024K
L3 cache:            36608K
NUMA node0 CPU(s):   0,1
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves ida arat pku ospke
sh-4.2$ 

sh-4.2$ free -h 
              total        used        free      shared  buff/cache   available
Mem:           3.8G        933M        975M        596K        1.9G        2.6G
Swap:            0B          0B          0B

sh-4.2$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        1.9G     0  1.9G   0% /dev
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           1.9G  588K  1.9G   1% /run
tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/nvme0n1p1  135G   74G   62G  55% /
/dev/nvme1n1    4.8G   36K  4.6G   1% /home/ec2-user/SageMaker
tmpfs           386M     0  386M   0% /run/user/1001
tmpfs           386M     0  386M   0% /run/user/1002
tmpfs           386M     0  386M   0% /run/user/1000

sh-4.2$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 85
model name      : Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz
stepping        : 7
microcode       : 0x5003901
cpu MHz         : 2500.004
cache size      : 36608 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves ida arat pku ospke
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit mmio_stale_data retbleed gds
bogomips        : 5000.00
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

processor       : 1
vendor_id       : GenuineIntel
cpu family      : 6
model           : 85
model name      : Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz
stepping        : 7
microcode       : 0x5003901
cpu MHz         : 2500.004
cache size      : 36608 KB
physical id     : 0
siblings        : 2
core id         : 0
cpu cores       : 1
apicid          : 1
initial apicid  : 1
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx avx512f avx512dq rdseed adx smap clflushopt clwb avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves ida arat pku ospke
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit mmio_stale_data retbleed gds
bogomips        : 5000.00
clflush size    : 64
cache_alignment : 64
address sizes   : 46 bits physical, 48 bits virtual
power management:

sh-4.2$ 
sh-4.2$ cat /proc/meminfo
MemTotal:        3943312 kB
MemFree:          999060 kB
MemAvailable:    2698344 kB
Buffers:            2848 kB
Cached:          1662408 kB
SwapCached:            0 kB
Active:           760748 kB
Inactive:        1465100 kB
Active(anon):        456 kB
Inactive(anon):   560732 kB
Active(file):     760292 kB
Inactive(file):   904368 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:                28 kB
Writeback:             0 kB
AnonPages:        560632 kB
Mapped:           259004 kB
Shmem:               596 kB
KReclaimable:     323324 kB
Slab:             441656 kB
SReclaimable:     323324 kB
SUnreclaim:       118332 kB
KernelStack:        3312 kB
PageTables:         8468 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     1971656 kB
Committed_AS:    1215416 kB
VmallocTotal:   34359738367 kB
VmallocUsed:       13400 kB
VmallocChunk:          0 kB
Percpu:             1352 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:      130984 kB
DirectMap2M:     2953216 kB
DirectMap1G:     1048576 kB

sh-4.2$ uname -a
Linux ip-172-16-60-113.ec2.internal 5.10.235-227.919.amzn2.x86_64 #1 SMP Sat Apr 5 16:59:05 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

sh-4.2$ cat /etc/os-release
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"
SUPPORT_END="2026-06-30"
sh-4.2$ 

sh-4.2$ # Get an IMDSv2 token (valid for 21600 seconds = 6 hours)
sh-4.2$ TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    56  100    56    0     0   9636      0 --:--:-- --:--:-- --:--:-- 11200
sh-4.2$ 
sh-4.2$ # Use the token to query the instance type
sh-4.2$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-type
t3.mediums
