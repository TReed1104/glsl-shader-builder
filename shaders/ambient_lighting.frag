#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

#include components/lighting_uniforms.glsl

void main() {
    vec3 ambient = (ambientStrength * lightingColor) * fragmentColour;
    outputColour = vec4(ambient, 1.0);
}