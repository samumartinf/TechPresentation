# European Client Forum
This is a short repo for the ECF presentation on the technology side. I have decided to test out manim-slides for the presentation. I will write down the requirements for this to work.


## Requirements
1. Install ffmpeg
2. Install manimgl and manim-slides

## Generating Slides and Videos

To generate the slides and videos for the presentation, follow these steps:

1. **Render the presentation**: Use the following command in your terminal to render the slides and videos using manim-slides:
   ```bash
   manim-slides render .\presentation.py ProtoBufVisualization
   ```

2. **Create a PowerPoint presentation** (optional): If you want to convert your slides to PowerPoint format, you can use:
   ```bash
   manim-slides convert --to=pptx ProtoBufVisualization presentation.pptx
   ```

3. **Generate a static PDF** (optional): For backup slides, you can create a PDF with:
   ```bash
   manim-slides convert --to=pdf ProtoBufVisualization presentation.pdf
   ```

4. **Output files**: The generated slides will be saved in the `slides/` directory, and the video files will be saved in the `media/videos/` directory.

Make sure to adjust the commands according to your specific needs and configurations.

