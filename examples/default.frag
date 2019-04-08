#version 330
in vec3 fragmentColour;

out vec4 outputColour;

#include examples/global_uniforms.glsl

#include examples/global_functions.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}