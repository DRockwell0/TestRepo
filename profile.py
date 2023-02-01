import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
node.routable_control_ip = "true"

#part 0 of instructions 
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y apache2"))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl status apache2'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo ufw allow "Apache Full"'))

#part 1 
node.addService(rspec.Execute(shell="/bin/sh", command='sudo a2enmod ssl'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo systemctl restart apache2'))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
