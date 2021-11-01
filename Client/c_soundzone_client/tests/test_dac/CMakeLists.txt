cmake_minimum_required(VERSION 3.16) # CMake version check
project(test_dac_project VERSION 0.0.1) # Create project "test_project"
set(CMAKE_CXX_STANDARD 20) # Enable c++14 standard

set(SOURCES
        test_dac.cpp
        ../../src/test_src.cpp
        ../../src/alsadriver.cpp
        )

# Add main.cpp file of project root directory as source file
set(${PROJECT_NAME} test_dac.cpp)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(${PROJECT_NAME} ${SOURCES})

# Set the directories that should be included in the build command for this target
target_include_directories(${PROJECT_NAME}
        PRIVATE
        ../../include
        )

# Link libraries to project
target_link_libraries(${PROJECT_NAME} ${myasoundlib} BCM2835 datatransport_lib)