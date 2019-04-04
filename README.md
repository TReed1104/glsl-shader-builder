# glsl-shader-builder
GLSL shader builder is a lightweight Python CLI for compiling multiple GLSL "component" files into a single GLSL Vertex or fragment shader to be used by OpenGL.

By default GLSL does not support "include" or "require" like other shader languages (HLSL or Unity) do. This means to developers have to implement the same variables and functions multiple times to re-use them. The aim of this program is to get around that limitation by allowing users to create multiple "component" files and compile them down into a single file without re-writing the same code over and over.

