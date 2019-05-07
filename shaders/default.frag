#version 330
#include components/fragment_in.glsl

#include components/fragment_out.glsl

#include components/global_uniforms.glsl

void main() {
	outputColour = vec4(fragmentColour, 1.0f);
}
