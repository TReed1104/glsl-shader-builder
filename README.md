# Ivaldi GLSL builder
Ivaldi is a lightweight python script used to compile multiple glsl component files into a single shader source file to be used by OpenGL.

Ivaldi takes it's name from the Dwarven smiths from Norse Mythology

## The Aim
GLSL as a language itself has no understanding of files, so does not support preprocessor directives like "#include", "import" or "requires". This means that developers have to reimplement or copy the same variables and functions multiple times in order to reuse their functionality across each of their shaders. **Ivaldi** aims to fix this issue by acting as a preprocessing script, used to compile multiple GLSL source files down into single source file to be loaded and compiled in any OpenGL program.

## Usage
### Terms
* Shader source file - Your main GLSL source code, in which you define your "#include" directives to be used by Ivaldi. (See "shaders/default.vert" within the repository as an example)
* Shader component files - Your reusable pieces of GLSL code, the files where you define your functions or common variables which are to be compiled down into main shader source files. (See "components/global_uniforms.glsl" within the repository as an example)

### Guide
```bash
python Ivaldi.py [-h] (-i INPUT | -a INPUT_DIRECTORY) [-o OUTPUT]
python Ivaldi.py [--help] (--input INPUT | --all INPUT_DIRECTORY) [--output OUTPUT]
```
* -h, --help - Show the help message and exit
* -i INPUT, --input INPUT - Specify the GLSL source file to compile.
* -a INPUT_DIRECTORY, --all INPUT_DIRECTPRY - Compile all shaders found in the specified directory. The default value for this argument is 'shaders'. Files compiled by this mode use their source file names.
* -o OUTPUT, --output OUTPUT - Where to output the compiled shader to. If --all is used, this argument will be ignored.

Example:
```bash
python Ivaldi.py -h
python Ivaldi.py -i shaders\default.vert
python Ivaldi.py -a shaders
python Ivaldi.py -i shaders\default.vert -o compiled_shader.vert
```

## Naming conventions
### Shader source files
The Ivaldi project follows the file naming conventions specified by the "Glslang" guidelines [(found here)](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/).

These are defined as the following:
* .vert - a vertex shader
* .tesc - a tessellation control shader
* .tese - a tessellation evaluation shader
* .geom - a geometry shader
* .frag - a fragment shader
* .comp - a compute shader

### Shader component files
For your shader component files, we ask that you use the ".glsl" file extension. This extension was chosen so that your GLSL functions and variables are correctly identified by most modern IDEs as the correct languages.
