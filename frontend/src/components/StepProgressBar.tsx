import React from "react";

type StepProgressBarProps = {
  stepNames: string[];
  stepCompleted: number;
};

export default function StepProgressBar(props: StepProgressBarProps) {
  return (
    <div className="flex justify-between">
      {props.stepNames.map((name, index) => {
        return <div className="relative flex flex-col align-center grow"></div>;
      })}
    </div>
  );
}
