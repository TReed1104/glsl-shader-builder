# Ivaldi, The GLSL Preprocessor
Ivaldi is a python preprocessing script, allowing for the use of "C-like" include directives in GLSL. This allows for the use of reusable GLSL component files in order to encourage and allow the re-usability of code.

Ivaldi takes it's name from the Dwarven smiths from Norse Mythology

<br>

---

## The Aim
GLSL as a language has no comprehension of files or file systems, so therefore does not support preprocessor directives like "#include", "import" or "requires". This means that developers are required to reimplement or copy the same variables and functions multiple times in order to reuse their functionality across each of their shaders.

**Ivaldi** aims to fix this issue by acting as a preprocessing script, used to compile multiple GLSL shader components files into single source files to be loaded by modern OpenGL programs.

<br>

---

## Terminology
* Shader source file - The main GLSL source code, in which you define your "#include" directives to be used by Ivaldi.
* Shader component files - The reusable pieces of GLSL code, the files in which functions or common variables are defined prior to being compiled into the final shader source code.

<br>

---

## Usage Guide
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
python Ivaldi.py -i glsl-shaders\source\default.vert
python Ivaldi.py --input glsl-shaders\source\default.vert
python Ivaldi.py -a
python Ivaldi.py --all
python Ivaldi.py -a glsl-shaders\source
python Ivaldi.py --all glsl-shaders\source
python Ivaldi.py -i glsl-shaders\source\default.vert -o compiled_shader.vert
python Ivaldi.py --input glsl-shaders\source\default.vert --output compiled_shader.vert
```

<br>

---

## Code Example
### Shader Component - fragment_in.glsl ([available here](https://github.com/TReed1104/glsl-shaders/blob/master/components/fragment_in.glsl))
```GLSL
// Generic In variables for a fragment shader (mesh colour and TexCoords)
in vec3 fragmentColour;
in vec2 UV;
in vec3 normal;
```

### Shader Component - fragment_out.glsl ([available here](https://github.com/TReed1104/glsl-shaders/blob/master/components/fragment_out.glsl))
```GLSL
// Generic Out variables for a fragment shader
out vec4 outputColour;
```

### Shader Component - global_uniforms.glsl ([available here](https://github.com/TReed1104/glsl-shaders/blob/master/components/global_uniforms.glsl))
```GLSL
// Universal uniforms, these match shadertoys
uniform vec3 iResolution;
uniform float iTime;
uniform vec4 iMouse;
```

### Shader Source File - default.frag ([available here](https://github.com/TReed1104/glsl-shaders/blob/master/source/default.frag))
```GLSL
#version 330
#include glsl-shaders/components/fragment_in.glsl

#include glsl-shaders/components/fragment_out.glsl

#include glsl-shaders/components/global_uniforms.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}
```

### Ivaldi Compiled Output - default.frag
```GLSL
#version 330
// Generic In variables for a fragment shader (mesh colour and TexCoords)
in vec3 fragmentColour;
in vec2 UV;
in vec3 normal;

// Generic Out variables for a fragment shader
out vec4 outputColour;

// Universal uniforms, these match shadertoys
uniform vec3 iResolution;
uniform float iTime;
uniform vec4 iMouse;

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}
```

<br>

---

## File Naming Conventions
### Shader Source Files
The Ivaldi project adheres to the file naming conventions specified by the "Glslang" guidelines ([found here](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/)).

These are defined as the following:
* .vert - a vertex shader
* .frag - a fragment shader
* .tesc - a tessellation control shader
* .tese - a tessellation evaluation shader
* .geom - a geometry shader
* .comp - a compute shader

### Shader Component Files
For your shader component files, please use the ".glsl" file extension. This extension was chosen so that component files are correctly identified by most modern development environments as the being GLSL source code.

<br>

---

## Todo List:
The following functionality is currently intended for Ivaldi in the future.
* Implement the ability for ivaldi to run the compiled code through the GLSL reference compiler to ensure the compiled source is valid GLSL code.
* Expand ivaldi to allow #includes within its component files, this means handling recursive inclusions.
* Allow Ivaldi to handle component includes from non-relative directories easier.
