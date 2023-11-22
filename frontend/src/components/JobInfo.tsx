import React from "react";

enum JobStatus {
  NONE,
  APPLIED,
  SCREENING,
  INTERVIEW,
  ACCEPTED,
}

enum RejectionPoint {
  NONE,
  APPLIED,
  SCREENING,
  INTERVIEW,
}

type JobInfoProps = {
  employerName: string;
  employerEmail: string;
  employerIconUrl: string;
  status: JobStatus;
  rejection: RejectionPoint;
};

export default function JobInfo(props: JobInfoProps) {
  return (
    <div className="w-full bg-gray-100 rounded-xl p-4 flex flex-col"></div>
  );
}
