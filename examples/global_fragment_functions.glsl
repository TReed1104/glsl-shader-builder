float random(vec2 p) {
	// Pseudo random number generator from seed
	const vec2 r = vec2(23.1406926327792690, 2.6651441426902251);// e^pi (Gelfond's constant) & 2^sqrt(2) (Gelfond-Schneider constant)
	return fract(cos(mod(123456789.0f, 1e-7+256.0f * dot(p, r))));
}