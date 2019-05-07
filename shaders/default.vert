#version 330
#include components/vertex_in.glsl

#include components/vertex_out.glsl

#include components/mvp_uniforms.glsl

void main() {
	// Set our vertex output values, these are what we use inside the fragment shaders
	fragmentColour = vertexColor;
	UV = vertexUV;
	normal = vertexNormal;

	// Output the positional value after applying the transformation matrices
	gl_Position = u_projectionMatrix * u_viewMatrix * u_modelMatrix * vec4(vertexPosition, 1.0);
}
