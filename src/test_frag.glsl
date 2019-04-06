#version 330
in vec3 fragmentColour;

out vec4 outputColour;

#include src/global_uniforms.glsl

#include src/global_functions.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}