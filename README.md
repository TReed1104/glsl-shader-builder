# Ivaldi GLSL builder
Ivaldi is a lightweight python script used to compile multiple glsl component files into a single shader source file to be used by OpenGL.

Ivaldi takes it's name from the Dwarven smiths from Norse Mythology

## The Aim
GLSL as a language itself has no understanding of files, so does not support preprocessor directives like "#include", "import" or "requires". This means that developers have to reimplement or copy the same variables and functions multiple times in order to reuse their functionality across each of their shaders. **Ivaldi** aims to fix this issue by acting as a preprocessing script, used to compile multiple GLSL source files down into single source file to be loaded and compiled in any OpenGL program.

## Usage
Guide:
```bash
python .\Ivaldi.py [-i INPUT] [-o OUTPUT]
python .\Ivaldi.py [--input INPUT] [--output OUTPUT]
```
* INPUT   - The main GLSL file you wish to compile (the file including the #include preprocessors)
* OUTPUT  - The target location you wish to save the compiled GLSL source to.

Example:
```bash
python .\Ivaldi.py -i .\src\fragment_main.glsl -o basic_fragment.frag
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
