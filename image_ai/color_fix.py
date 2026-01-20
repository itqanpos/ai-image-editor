import cv2

def fix_colors(input_path, output_path):
    img = cv2.imread(input_path)
    result = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(output_path, result)
