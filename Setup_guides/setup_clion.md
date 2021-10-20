
# How to setup clion to remote host

1. Open project
2. Setup ToolChain for remote host
   1. File -> Settings -> Build, Execution, Deployment -> Toolchains
   2. Press the '+' sign
   3. Press 'Remote Host'
   4. Fill fields
      1. Name - "What ever you want to call it the toolchain"
      2. Credencials - Select/setup a SSH to the remote host
      3. The rest should automatically fill out (can take 2 min)
   5. Press "Apply"

![](photos/add_toolchain.png)

3. Setup CMake
   1. File -> Settings -> Build, Execution, Deployment -> CMake
   2. Press the '+' sign
   3. Fill fields
      1. Name - "What ever you want to call the maker"
      2. Build type - Debug or release, depends on what you need
      3. Toolchain - Select the toolchain you made before
   4. Press "Apply"
   
![](photos/add_cmake.png)

4. Setup deployment
   1. Select the entry whit the name of the toolchain you made
   2. Press "Mappings"
   3. Configure Deployment path


![](photos/clion_deployment.png)