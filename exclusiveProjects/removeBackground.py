import cv2
import numpy as np

def remove_background():
    background_color = (0, 255, 0)  # Green
    image_path = input("Address the first image with name file, please: ")
    output_path = input("Address the second image which you want to save: ")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return

    # Initialize mask
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define initial bounding rectangle
    rect = cv2.selectROI("Select the object", image, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()

    # Allocate memory for models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Apply grabCut algorithm
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Modify the mask
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Extract the foreground
    foreground = image * mask2[:, :, np.newaxis]

    # Create a green background
    background = np.full_like(image, background_color)
    background = background * (1 - mask2[:, :, np.newaxis])

    # Combine the foreground with the green background
    combined = foreground + background

    # Save the result
    cv2.imwrite(output_path, combined)
    print(f"Background removed and saved to: {output_path}")

remove_background()
