#version 330
in vec3 fragmentColour;

out vec4 outputColour;

#include shaders/global_fragment_uniforms.glsl

#include shaders/global_fragment_functions.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}