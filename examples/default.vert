#version 330
#include components/vertex_in.glsl

#include components/vertex_out.glsl

#include components/mvp_uniforms.glsl

void main() {
	fragmentColour = vertexColor;
	vec4 newPosition = vec4(vertexPosition, 1.0);
	gl_Position = u_projectionMatrix * u_viewMatrix * u_modelMatrix * newPosition;
	UV = vertexUV;
}
