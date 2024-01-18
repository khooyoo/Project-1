# Project-1

# ImageProcessor

The `ImageProcessor` class is a Python class designed to provide a set of image processing operations. It uses the Pillow library (`PIL`) for working with images. The class is intended to handle both color and black-and-white images.

## Usage

### Initialization

```python
from ImageProcessor import ImageProcessor

# Initialize with a default image file (girl_coffee.jpg)
processor = ImageProcessor()

# Initialize with a custom image file
processor = ImageProcessor('path/to/your/image.jpg')


### Image Processing Methods

#### 1. Add
```python
result_img = processor.add(image_path='path/to/additional/image.jpg', scale=2, offset=0)
```
Add another image to the current image. we can specify the path to the additional image, as well as optional parameters for scaling and offset.

#### 2. Reverse
```python
result_img = processor.reverse()
```
Invert the colors of the image.

#### 3. Gaussian Blur
```python
result_img = processor.gaussian_blur(intensity=10)
```
Apply Gaussian blur to the image. we can adjust the intensity of the blur.

#### 4. Contrast
```python
result_img = processor.contrast()
```
Apply contrast enhancement to the image.

#### 5. Find Edges
```python
result_img = processor.find_edges()
```
Detect edges in the image.

#### 6. Brightness
```python
result_img = processor.brightness(intensity)
```
Adjust the brightness of the image. The intensity parameter determines the level of brightness adjustment.

#### 7. Crop
```python
result_img = processor.crop(x1, y1, x2, y2)
```
Crop the image based on the specified coordinates of the top-left and bottom-right corners.

### Utility Methods

#### 1. Set Image
```python
processor.set_image(image_path='path/to/new/image.jpg')
```
Set the image to a new image file.

#### 2. Get Image
```python
current_img = processor.get_image()
```
Get the current image object.

#### 3. Show
```python
processor.show()
```
Show the current image.

## Notes

- All processing methods return the resulting image and update the internal state of the `ImageProcessor` object.
- The class uses the `copy()` method to avoid potential issues with mutable objects when updating the internal image state.

