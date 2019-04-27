# Ivaldi GLSL builder
Ivaldi is a lightweight python script used to compile multiple glsl component files into a single shader source file to be used by OpenGL.

Ivaldi takes it's name from the Dwarven smiths from Norse Mythology

## The Aim
GLSL as a language itself has no understanding of files, so does not support preprocessor directives like "#include", "import" or "requires". This means that developers have to reimplement or copy the same variables and functions multiple times in order to reuse their functionality across each of their shaders. **Ivaldi** aims to fix this issue by acting as a preprocessing script, used to compile multiple GLSL source files down into single source file to be loaded and compiled in any OpenGL program.

## Usage
Guide:
```bash
python .\Ivaldi.py [-h] [-i INPUT] [-o OUTPUT]
python .\Ivaldi.py [--help] [--input INPUT] [--output OUTPUT]
```
* -h, --help - Show the App's help guide
* -i INPUT, --input INPUT - Name of the GLSL file to compile
* -o OUTPUT, --output OUTPUT - Name of the file to out the compiled shader source to 

Example:
```bash
python .\Ivaldi.py -h
python .\Ivaldi.py -i .\shaders\default.vert
python .\Ivaldi.py -i .\shaders\default.vert -o compiled_shader.vert
```

## Naming Conventions
**WIP**

According to the "Glslang" guidelines [(Seen here)](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/), the correct file naming conventions are as follows:
* .vert - a vertex shader
* .tesc - a tessellation control shader
* .tese - a tessellation evaluation shader
* .geom - a geometry shader
* .frag - a fragment shader
* .comp - a compute shader
