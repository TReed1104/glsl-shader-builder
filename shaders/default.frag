#version 330
in vec3 fragmentColour;

out vec4 outputColour;

#include components/global_uniforms.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}
