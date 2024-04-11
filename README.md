
https://skinny-moose-664.notion.site/A-Review-of-3D-reconstruction-3D-model-generation-technique-for-various-anthropometric-body-part-9fabd13c7598478f8f2c0c724dc292bb?pvs=4

# A Review of 3D reconstruction(3D model generation)technique for various anthropometric body part.
# Abstract

This paper reviews the latest advancements in 3D model generation techniques for anthropometric body parts, emphasizing their significance in sports and health monitoring. We explore the integration of photogrammetry, Neural Radiance Fields (NeRFs), Gaussian splatting, and voxel hashing technologies that facilitate the precise measurement and visualization of body changes. Highlighted applications and tools include Agisoft Metashape, ColMap for photogrammetry; Luma AI, 3DPresso (ReconLabs) for NeRFs; and novel approaches in Gaussian splatting and voxel hashing for scalable real-time 3D reconstruction. The paper also addresses the determination of camera positions for accurate photo capture. By enabling users to overlay meshes on images for comparison and measurement, these technologies represent a leap forward in tracking muscle growth and body dimension changes, offering invaluable tools for athletes and health professionals.

# Introduction

In the quest to precisely measure the human body's anthropometric dimensions, various innovative approaches have been explored, leveraging advancements in digital imaging and computational algorithms. These endeavors aim to transcend the limitations of traditional methods, which often involve manually annotated markers and are labor-intensive, requiring significant expertise and resources. This paper synthesizes the progression from manual to digital techniques, particularly emphasizing the capabilities and potential of cutting-edge technologies for accurate 3D reconstruction and measurement of body parts.

Historically, methods such as single-camera stereo vision have demonstrated the feasibility of depth perception and distance measurement on mobile devices without the need for dual-camera configurations. This innovation marks a significant leap towards democratizing computer stereo vision, making it accessible on a wider array of devices. Furthermore, photogrammetry has been increasingly recognized for its utility in anthropometry, enabling the estimation of human height and mid-upper arm circumference (MUAC) with notable precision. These advancements underscore the shift towards non-invasive, scalable, and user-friendly techniques for body measurement.

Digital anthropometry has also emerged as a promising avenue, particularly with the development of platforms like Android, which automate body measurement using image processing algorithms. This approach not only simplifies the measurement process but also enhances its accessibility and applicability in various domains, including custom tailoring and ergonomic design. Concurrently, optical imaging technologies have facilitated the analysis of body size and shape through systems designed for personal use, such as the Naked Body Scanner (NBS), which competes favorably against conventional methods in terms of accuracy and convenience.

Despite these advancements, the precise measurement of specific body parts, particularly muscles like the biceps and triceps, poses additional challenges. Addressing this, our discussion extends to the application of photogrammetry, Neural Radiance Fields (NeRFs), Gaussian splatting, and voxel hashing. These technologies offer sophisticated means for creating high-quality 3D models, which are pivotal for accurate body measurement. While NeRFs present limitations in direct object length measurement, photogrammetry, with its capability to generate detailed point clouds, alongside Gaussian splatting and voxel hashing, provides a robust framework for precise anthropometric assessment.

**This paper aims to delve into the integration and application of these contemporary technologies for 3D reconstruction and measurement, highlighting their potential to revolutionize anthropometry.** By examining existing methods, programs, applications, and APIs that harness these technologies, we seek to elucidate their contributions to achieving more precise, reliable, and efficient measurement of human body dimensions.

# **Technologies for 3D reconstruction**

# 1. what is the 3D Reconstruction?

3D reconstruction is a process that translates observations of real-world objects into precise three-dimensional models. It harnesses various techniques like photogrammetry, laser scanning, and computer vision algorithms to capture the geometry and appearance of physical objects, enabling their digital representation. This technology plays a crucial role in diverse fields, including medical imaging, entertainment, heritage preservation, and sports science, by providing accurate and tangible representations of complex shapes and forms for analysis, visualization, and interaction.

# 2. 3D Reconstruction Using Voxels

Voxel reconstruction in 3D modeling employs a grid of voxels to represent space, simulating light interactions within a scene for rendering. It involves casting rays to intersect with this voxel grid, evaluating each voxel's color and density to calculate light transmittance. The process accumulates these interactions along the ray's path, utilizing alpha compositing to blend voxel contributions. This technique achieves detailed scene visualizations by accurately depicting how light is absorbed, scattered, and transmitted through various materials, offering a computationally efficient method for rendering complex 3D scenes.

- **Voxels**: The 3D space is discretized into a grid of voxels, each potentially holding values for properties like color and density. This voxel grid allows for a simplified representation of complex 3D geometries and their optical properties.
- **Density and Transmittance**: Each voxel's density affects how much light can pass through it. High density may result in lower transmittance (more absorption or scattering), affecting the color and intensity of light that reaches the viewer.
- **Accumulated Transmittance**: As a ray travels through multiple voxels, the cumulative effect of voxel densities along its path determines the overall transmittance. This is crucial for rendering realistic scenes, as it simulates the attenuation of light through mediums like fog, smoke, or interiors of objects.
- **Alpha Compositing**: The color contribution of each voxel along a ray's path is combined using alpha compositing, based on the voxel's color, density, and the accumulated transmittance up to that point. This step produces the final color value for the corresponding pixel on the image plane.

# 3. Mesh extraction

Mesh extraction transforms a volumetric representation of a scene or object into a ploygonal mesh by predictin density across a 3D space, identifying the isosurface that defines the object’s boundary, and tringulating this surface into a mesh using the marching cubes algorithm. this technique brideges the gap between volumetric data and surface-based representation, enabling the visualization and manpulation of complex 3D shapes.

- **Marching Cubes Algorithm**: This is a classic computer graphics algorithm used to extract a polygonal mesh of an isosurface from a three-dimensional scalar field (such as the density field generated by the voxel model). The algorithm works by iterating over the voxel grid, examining the density values at the corners of each cube (formed by adjacent voxels), and determining where the surface intersects that cube based on those values.
- **Isosurface Extraction**: The marching cubes algorithm identifies the surface of the object (isosurface) by determining where the density values cross a certain threshold (isosurface value). This threshold is chosen to differentiate between the inside and outside of the object, effectively capturing the boundary where the object material transitions from solid to empty space.
- **Vertices and Triangles Generation**: For each cube where an intersection with the isosurface is detected, the algorithm computes the precise positions of the surface intersection points along the edges of the cube. It then uses a pre-defined lookup table to triangulate these points, producing a set of vertices (points in 3D space) and triangles (connecting groups of three vertices) that approximate the surface within that cube. The process is repeated for all cubes in the grid, and the resulting vertices and triangles are combined to form a continuous mesh representing the entire isosurface.

# 4. Photogrammetry

Photogrammetry, combining the essence of photography and measurement, stands as a cornerstone in accurately reconstructing 3D models from images. It's essential across diverse domains, notably in sports and health for creating lifelike representations of anthropometric body parts. This method involves analyzing images captured from various angles to deduce the 3D structure of objects, akin to human depth perception. Despite its broad applicability, challenges arise with textureless surfaces or under low-light conditions. Nonetheless, photogrammetry remains an invaluable technique for producing detailed digital replicas, significantly benefiting fields requiring precise dimensional analysis. Photogrammetry reconstructs 3D models by taking multiple photographs of an object from different angles. The process involves measuring and recording the position of surface points and their attributes (like color and texture) from these images. Algorithms analyze the images to estimate the camera positions and create a point cloud representing the object’s surface. This point cloud is then densified and converted into a polygon mesh, onto which textures derived from the photographs are mapped, producing a photorealistic 3D model. In photogrammetry, algorithms such as Structure from Motion (SfM) and Multi-View Stereo (MVS) are commonly used. SfM estimates camera positions and creates a sparse point cloud by analyzing the movement of features across a set of images. MVS then refines this information, comparing images from the estimated camera positions to build a dense point cloud representing the object's surface in detail. These processes leverage computer vision and machine learning techniques to deduce 3D structures from 2D images.

# 5. Neural Radiance field

Although voxel models provide a straightforward and intuitive approach to 3D modeling, they suffer from a trade-off between memory usage and resolution. High-resolution models require exponentially more memory, making it challenging to model detailed scenes without vast computational resources. However, by leveraging the continuous function approximation capabilities of neural networks, NeRF offers superior detail, efficiency, and flexibility, making it a better choice for high-quality 3D reconstruction and novel view synthesis in many applications.

NeRF works by optimizing a continuous volumetric scene function with a sparse set of input views, representing a scene through a deep network that processes 5D coordinates (spatial location and viewing direction) to output volume density and view-dependent emitted radiance. This method synthesizes views by querying these coordinates along camera rays, employing volume rendering techniques to project output colors and densities into images. The optimization of neural radiance fields is facilitated by the natural differentiability of volume rendering, requiring only images with known camera poses for input.

# 6. Gaussian-splatting

3D Gaussian Splatting enhances real-time radiance field rendering by streamlining scene representation. Unlike traditional methods that require extensive computation for each view, Gaussian Splatting simplifies this by aggregating scene information into splats, which are efficiently processed. This results in significantly faster rendering times compared to NeRFs, which calculate light interactions in a dense 3D grid, making Gaussian Splatting more practical for real-time applications without compromising visual quality. This approach offers a balance between performance and detail, crucial for interactive and immersive experiences.

# 7. Voxel Hashing

Voxel hashing is a technique for real-time 3D reconstruction that manages large-scale environments efficiently by using a data structure called a hash table to store and access volumetric data (voxels) dynamically. This method allows for the rapid retrieval and update of voxel information, facilitating the real-time reconstruction of detailed 3D models from sensor data. It's particularly advantageous for handling extensive scenes where memory efficiency and fast access to spatial data are critical, making it a significant advancement over traditional voxel storage methods for scalable and real-time 3D modeling.

# Available Tools

# Luma AI

Luma AI, leveraging Neural Radiance Fields (NeRFs) technology, revolutionizes the creation of 3D models with its user-friendly mobile application and Unreal Engine plugin. By guiding users through an intuitive process, Luma AI makes capturing detailed and realistic 3D representations from video captures a breeze, suitable for a plethora of applications including gaming, ecommerce, social media, marketing, and real estate ([Luma AI](https://lumalabs.ai/luma-api)) ([Dataconomy](https://dataconomy.com/2023/06/19/what-is-luma-ai/)) ([ExpertBeacon](https://expertbeacon.com/luma-ai/)). Its API is adept at processing multi-level video inputs to produce outputs ranging from interactive 3D scenes to pre-rendered 360 images and videos, thereby optimizing volumetric representation of scenes for games and virtual production ([Luma AI](https://lumalabs.ai/luma-api)) ([CG Channel](https://www.cgchannel.com/2023/04/use-nerfs-in-unreal-engine-with-luma-ais-new-plugin/)). This capability is especially beneficial for visualizing dynamic changes, such as body dimensions or muscle growth over time, providing a cost-effective solution at just $1 per 3D model with rapid processing times ([Dataconomy](https://dataconomy.com/2023/06/19/what-is-luma-ai/)) ([ExpertBeacon](https://expertbeacon.com/luma-ai/)). This blend of affordability, speed, and versatility positions Luma AI as a pioneering force in democratizing 3D model creation across industries.

# MetaRECON(ReconLabs)

MetaRECON by ReconLabs addresses the challenges faced by traditional photogrammetry in reconstructing 3D models of objects with textureless or reflective surfaces. This advanced 3D reconstruction engine merges conventional photogrammetry with AI technologies to yield high-quality surface reconstructions. It capitalizes on Neural Radiance Fields (NeRF) for volume field training, significantly enhancing the detail and stability of the resulting 3D mesh through the refinement of NeRF results into an SDF function, making it a potent tool for accurate and stable 3D reconstructions of complex surfaces.

# PlicAR(ReconLabs)

PlicAR by ReconLabs marks the beginning of 3D eCommerce, offering a web-based service that transforms eCommerce products into 3D and AR models for diverse applications like digital showrooms and catalogs. Leveraging AI to generate lifelike models from actual video footage, PlicAR ensures high authenticity at a reasonable cost. It simplifies the creation and utilization process, significantly reducing the effort and expense typically associated with product photography and page detailing.

# 3DPresso(ReconLabs)

3DPresso by ReconLabs is an AI-based 3D creation solution designed for easy and quick transformation of 2D video captures into high-quality 3D models, suitable for a range of applications including AR shopping. This web-based platform enhances workflow efficiency by automating the generation of 3D models with AI, offering real-time web-based visualization, and facilitating the sharing of 3D assets. It significantly simplifies the process of creating 3D content, making it accessible even through simple smartphone captures, thereby democratizing 3D model creation for creators and professionals alike.

# Nerf_PL

Nerf_PL is a practical implementation of the original NeRF model using PyTorch, aimed at simplifying the process of 3D reconstruction. It's highlighted for its accessibility to beginners, offering an easier-to-understand alternative to TensorFlow implementations. This repository not only reproduces NeRF but also introduces additional features like 3D mesh extraction and integration with Unity for real-time applications. Its straightforward installation and minimal dependencies make it a go-to for those new to NeRF, aiming to understand the code and apply it to real-world scenarios efficiently.

# Nerf Studio

Nerf Studio is a notable project within the NeRF community, celebrated for its ease of installation and broad applicability despite a somewhat complex codebase. It enhances the NeRF framework by offering tools for geometry exploration, like SDA fusion and mesh extraction, and introduces innovative features for camera parameter refinement. The tool provides a selection of different models and techniques, such as vanilla NeRF, MIP-NeRF, and several others. It even includes innovative features like instant GPU for accelerated processing and semantic NeRF for incorporating semantic information into the 3D models.

# SDF Studio

SDF Studio, evolving from Nerf Studio, specializes in surface reconstruction, offering advanced methods over volumetric rendering for more accurate surface depiction. It maintains Nerf Studio's structure, ensuring ease of transition between the two, and includes various methods like SDF facto for detailed surface modeling. This makes SDF Studio ideal for reconstructing environments like rooms, suggesting potential for future integration with Nerf Studio into a unified framework.

# Instant-NGP

Instant-NGP, heralded by Time Magazine as one of 2022's best inventions and developed by Nvidia, stands out for its rapid 3D model generation. Leveraging the tiny CUDA engine, it requires specific hardware and software setups. Nvidia also introduced a no-code interface, simplifying model viewing without installation hassles. This innovation represents a significant leap in accessible, efficient 3D modeling, although it may present initial setup challenges. For those seeking easier alternatives, other libraries with simpler installation processes and PyTorch implementations are recommended.

# NGP-PL

Instant-NGP, highlighted for its rapid 3D model generation and reliance on CUDA for speed, simplifies PyTorch implementations. Despite requiring specific libraries like tiny CUDA and torch scatter, it's user-friendly and supports various data sets, including those from significant papers like Nerf++. Its efficiency and the provided GUI enhance interaction with models, making it an excellent choice for those seeking to dive into 3D modeling with modern requirements.

# NerfAcc

NerfAcc is a repository focused on accelerating NeRF model training and rendering, making it more efficient than traditional NeRF implementations. It introduces occupancy grids and other optimizations to reduce training times significantly, from days to just hours. Its approach allows for plug-and-play functionality, simplifying the integration of new models or improvements. This repository stands out for its user-friendly design and detailed documentation, making it accessible for various needs in the NeRF community.

# Result

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/23ea65cd-4135-49bc-a759-3bd45dcab458/f3063644-e790-42f6-8a53-2a46ad74ff64/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/23ea65cd-4135-49bc-a759-3bd45dcab458/63347133-9d7a-4e75-9062-9698aa2b7b08/Untitled.png)

[Triceps - Created by @ChanghunKim with Luma](https://lumalabs.ai/capture/8e4b3f53-1cd5-4f2f-836a-edac41affc77)

# References :

Agisoft Metashape:

[https://www.agisoft.com/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkFwLUJUM01ja0w2V0xoQWtfbEs5bWNxbWx3UXxBQ3Jtc0tseGx2YVpsbXBkbm13MWlocmFDWmd6Q1RWOVc3U0txVHZyaVhsY3p4aWtuU0ZWamdvakZqckZKWG9jbG1xb0F3ajJ4aWl6VnlfNmVGWE4zTVV4dkpBaDJhNWdlMDZUSTRXdUM4eGdnOURwYXFyNzg4RQ&q=https%3A%2F%2Fwww.agisoft.com%2F&v=KFOy354zf9E)

NerfStudio:

[https://docs.nerf.studio/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE0ySXI4X3pjZHFqbHdfUWVLNDVBaTdDZGZLd3xBQ3Jtc0tuTlI4Y0NrcXExTHM3am1hWVZxdUJUV2tfcHBlOXRYQmNTV1ZfU2FFR29EQXpnd1UzQkRuNHBMU25CbEMzM3NJNHVLY0xKOUNaY3o3SEJFMTFxT1B5N3RNeFV3STk3QzA0T19kSmppWnBnZFYxUTB1bw&q=https%3A%2F%2Fdocs.nerf.studio%2F&v=KFOy354zf9E)

3D Gaussian Splatting for Real-Time Radiance Field Rendering:

[https://github.com/graphdeco-inria/ga...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGQ4UU5iR1Bya2RpSjR1Q0Y1aEJ3VXFjRW5NZ3xBQ3Jtc0ttTXFSckFXQ1FGYXBCN0VaYXlJblozR19PMno4RjVtZ2NndFdKNHZIYnlPYzJ4VS1OdE5MTVdPNmROaTFOX2NmUFY1S1hCc2hFa3pqN1FMNWpILWlJQTBpRVp2MTl6YWtFNElyb1ZWOTBSRTVhaFZWNA&q=https%3A%2F%2Fgithub.com%2Fgraphdeco-inria%2Fgaussian-splatting&v=KFOy354zf9E)

Aras-p’s Unity Project:

[https://github.com/aras-p/UnityGaussi...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEtYNWVnRnJHNGhnUWZoOWlXcjFPOExMWUdCQXxBQ3Jtc0tua0tGTWNrZ25Ba20yWGUwVENRZWladEEwSU9tWWlnVlpoeFdVNTRrTkpVVTJNWl9hcW01UnFpWDVfall5ZU1xV2EtdFNET1VBbWs2LVJ4UnR5b3pJbHNmT2xTZXlWV3VLVFRPT2h0MTFUZ1piYWhfdw&q=https%3A%2F%2Fgithub.com%2Faras-p%2FUnityGaussianSplatting&v=KFOy354zf9E)

[Luma AI - Interactive Scenes](https://lumalabs.ai/interactive-scenes)

[Fit 3D Body Scanner for Gyms](https://www.youtube.com/watch?v=6O7OM94Nrqk)

[176-cameras 3d-scan full-body photogrammetry demo](https://youtu.be/M2wmyf28I5k?si=XdAMpjO4lFd77p_J)

[Photogrammetry / 3d-scan software - connect, control and trigger up to 250 cameras — Xangle Camera Server](https://xanglecs.com/photogrammetry)

[Face / Facs / Head 3d-scan photogrammetry studio in Montréal — Xangle Studio](https://xanglestudio.com/head-scan)

[Testing our new full-body 3D scanner!](https://youtu.be/TmAcBOn473Y?si=6OmOmkTi-bbKb7Tc)

[The Difference Between NeRF And Photogrammetry 3D Scan](https://www.youtube.com/watch?v=m9JyKQTxTY4)

[RECON Labs](https://en.reconlabs.ai/)

[3Dpresso](https://3dpresso.ai/)

[[R:세미나] 리콘랩스 오픈 세미나 #3, ‘NeRF & Gaussian Splatting’ : 리콘랩스(RECON Labs)](https://www.reconlabs.ai/blog/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6NTt9&bmode=view&idx=17059184&t=board)

[Making measurements of a 3D Photoscan model](https://www.agisoft.com/forum/index.php?topic=2864.0)

[3D viewer](https://www.agisoft.com/forum/index.php?topic=2134.0)

[ABViewer | How to measure a 3D model](https://kr.cadsofttools.com/products/abviewer/tutorials/how-to-measure-3d-models/)

[Measure objects, distances, and areas—3D Workflows | Documentation](https://doc.arcgis.com/en/3d/workflows/analysis/measuring-objects-distances-and-areas-in-3d.htm)

[Measuring objects with Computer Vision and 3D reconstruction.](https://eidos-ai.medium.com/measuring-objects-with-computer-vision-and-3d-reconstruction-fb91600cb237)