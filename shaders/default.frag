#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}
