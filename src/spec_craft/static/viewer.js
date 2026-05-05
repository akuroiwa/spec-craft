let scene, camera, renderer, controls, mesh;

function init() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f0f0);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 100;

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;

    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(1, 1, 1).normalize();
    scene.add(directionalLight);

    window.addEventListener('resize', onWindowResize, false);

    // Get model from query param
    const urlParams = new URLSearchParams(window.location.search);
    const modelPath = urlParams.get('model');
    if (modelPath) {
        loadSTL(modelPath);
    }

    animate();
}

function loadSTL(path) {
    const statusEl = document.getElementById('status');
    const filenameEl = document.getElementById('filename');
    
    filenameEl.textContent = `Model: ${path}`;
    statusEl.textContent = "Loading...";

    const loader = new THREE.STLLoader();
    // Path is relative to the build/ directory served at /build/
    const fullPath = `/build/${path}`;

    loader.load(fullPath, function (geometry) {
        const material = new THREE.MeshStandardMaterial({ color: 0x0077ff, roughness: 0.5, metalness: 0.2 });
        
        if (mesh) scene.remove(mesh);
        
        mesh = new THREE.Mesh(geometry, material);
        
        // Center the model
        geometry.computeBoundingBox();
        const center = new THREE.Vector3();
        geometry.boundingBox.getCenter(center);
        mesh.position.sub(center);
        
        scene.add(mesh);
        
        statusEl.textContent = "Ready";
        statusEl.className = "";
    }, function (xhr) {
        if (xhr.lengthComputable) {
            const percent = (xhr.loaded / xhr.total) * 100;
            statusEl.textContent = `Loading: ${Math.round(percent)}%`;
        }
    }, function (error) {
        console.error(error);
        statusEl.textContent = "Error loading model";
        statusEl.style.color = "red";
    });
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

init();
