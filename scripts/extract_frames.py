import argparse
import os
from pathlib import Path
import cv2


def extract_frames(video_folder: str, output_folder: str, frames_per_video: int = 10) -> None:
    os.makedirs(output_folder, exist_ok=True)

    video_files = list(Path(video_folder).rglob("*.avi"))
    print(f"Found {len(video_files)} videos")

    total_frames = 0

    for video_idx, video_path in enumerate(video_files):
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            print(f"Warning: could not open {video_path}")
            continue

        total_frames_in_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = max(1, total_frames_in_video // frames_per_video)

        saved = 0
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0 and saved < frames_per_video:
                frame_filename = f"{video_path.stem}_frame_{saved:03d}.jpg"
                output_path = os.path.join(output_folder, frame_filename)
                cv2.imwrite(output_path, frame)
                saved += 1
                total_frames += 1

            frame_count += 1

        cap.release()

        if (video_idx + 1) % 50 == 0:
            print(f"Progress: {video_idx + 1}/{len(video_files)}, Total frames extracted: {total_frames}")

    print(f"Done! Extracted {total_frames} frames.")


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract N frames from each .avi video in a folder tree.")
    parser.add_argument("--video_folder", required=True, help="Path to folder containing .avi videos (searched recursively).")
    parser.add_argument("--output_folder", required=True, help="Path to output folder for extracted frames.")
    parser.add_argument("--frames_per_video", type=int, default=10, help="How many frames to save per video.")
    return parser


if __name__ == "__main__":
    args = build_argparser().parse_args()
    extract_frames(args.video_folder, args.output_folder, args.frames_per_video)
