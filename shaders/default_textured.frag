#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

#include components/texture_uniforms.glsl

void main() {
	if (u_hasTexture) {
		outputColour = texture2D(u_textureSampler, UV);
	}
	else {
		// Texturing has not been setup, use the colour buffer.
		outputColour = vec4(fragmentColour, 1.0f);
	}
}