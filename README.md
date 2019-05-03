# Ivaldi GLSL builder
Ivaldi is a lightweight python script used to compile multiple glsl component files into a single shader source file to be used by OpenGL.

Ivaldi takes it's name from the Dwarven smiths from Norse Mythology

<br>

---

## The Aim
GLSL as a language itself has no understanding of files, so does not support preprocessor directives like "#include", "import" or "requires". This means that developers have to reimplement or copy the same variables and functions multiple times in order to reuse their functionality across each of their shaders. **Ivaldi** aims to fix this issue by acting as a preprocessing script, used to compile multiple GLSL source files down into single source file to be loaded and compiled in any OpenGL program.

<br>

---

## Terminology
* Shader source file - Your main GLSL source code, in which you define your "#include" directives to be used by Ivaldi.
* Shader component files - Your reusable pieces of GLSL code, the files where you define your functions or common variables which are to be compiled down into main shader source files.

<br>

---

## Code Example
### Shader Component
#### File - fragment_in.glsl ([available here](https://github.com/TReed1104/ivaldi-glsl-builder/blob/master/components/fragment_in.glsl))
```GLSL
// Generic In variables for a fragment shader (mesh colour and TexCoords)
in vec3 fragmentColour;
in vec2 UV;
```

### Shader source file
#### File: default.frag ([available here](https://github.com/TReed1104/ivaldi-glsl-builder/blob/master/shaders/default.frag))
```GLSL
#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}

```

<br>

---

## Usage guide
Arguments:
```bash
python Ivaldi.py [-h] (-i INPUT | -a INPUT_DIRECTORY) [-o OUTPUT]
python Ivaldi.py [--help] (--input INPUT | --all INPUT_DIRECTORY) [--output OUTPUT]
```
* -h, --help - Show the help message and exit
* -i INPUT, --input INPUT - Specify the GLSL source file to compile.
* -a INPUT_DIRECTORY, --all INPUT_DIRECTPRY - Compile all shaders found in the specified directory. The default value for this argument is 'shaders'. Files compiled by this mode use their source file names.
* -o OUTPUT, --output OUTPUT - Where to output the compiled shader to. If --all is used, this argument will be ignored.

Examples:
```bash
python Ivaldi.py -h
python Ivaldi.py -i shaders\default.vert
python Ivaldi.py -a shaders
python Ivaldi.py -i shaders\default.vert -o compiled_shader.vert
```

<br>

---

## File Naming conventions
### Shader source files
The Ivaldi project follows the file naming conventions specified by the "Glslang" guidelines ([found here](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/)).

These are defined as the following:
* .vert - a vertex shader
* .frag - a fragment shader
* .tesc - a tessellation control shader
* .tese - a tessellation evaluation shader
* .geom - a geometry shader
* .comp - a compute shader

### Shader component files
For your shader component files, we ask that you use the ".glsl" file extension. This extension was chosen so that component files are correctly identified by most modern development environments as the being GLSL source code.

<br>

---

## Todo List:
The following are functionality to be added to ivaldi in the future.
* Implement the ability for ivaldi to run the compiled code through the GLSL reference compiler to ensure the compiled source is valid GLSL code.
* Expand ivaldi to allow #includes within its component files, this means handling recursive inclusions.
