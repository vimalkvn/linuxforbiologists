 #!/usr/bin/env bash

# You will need to run zerofree on the disk before running
# this script

vmdk=$1
vmdk_base=$(basename $vmdk .vmdk)

vdi=${vmdk_base}.vdi
vmdk_compact=${2:-${vmdk_base}-compact.vmdk}

echo "\nConverting $vmdk to $vdi"
VBoxManage clonemedium --format VDI $vmdk $vdi

echo "\nCompacting $vdi"
VBoxManage modifymedium --compact $vdi

echo "\nConverting $vdi to $vmdk_compact"
VBoxManage clonemedium --format VMDK $vdi $vmdk_compact
