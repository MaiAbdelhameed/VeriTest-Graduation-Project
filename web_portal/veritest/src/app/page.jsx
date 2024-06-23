// component imports

import Link from "next/link";
import Logo from "@/components/Logo_component";
import Subtext from "@/components/subtext_component";

export default function Home() {
  return (
    <div>
      <div className="container">
        {/* logo component */}
        <Logo />
        {/* subtext component */}
        <Subtext />
        <div className="row">
          <div className="col d-flex flex-column align-items-center ">
            {/* mode 1 button and details paragraph */}

            <Link href={"/mode1"}>
              <button
                type="button"
                className="mt-2 mb-2 btn btn-lg btn-success"
              >
                Mode 1
              </button>
            </Link>
            <p className="text-center">
              Generate a Verilog testbench by uploading the Verilog file and a
              python golden model
            </p>
          </div>

          <div className="col d-flex flex-column align-items-center ">
            {/* mode 2 button and details paragraph */}
            <Link href={"/mode2"}>
              <button
                type="button"
                className=" mt-2 mb-2 btn btn-lg btn-success"
              >
                Mode 2
              </button>
            </Link>
            <p className="text-center">
              Generate a Verilog testbench by uploading the Verilog file and a
              JSON specifications file
            </p>
          </div>

          <div className="col d-flex flex-column align-items-center ">
            {/* mode 3 button and details paragraph */}

            <Link href={"/mode3"}>
              <button
                type="button"
                className=" mt-2 mb-2 btn btn-lg btn-success"
              >
                Mode 3
              </button>
            </Link>

            <p className="text-center">
              Upload a verilog file and our AI model will generate a testbench
              for you
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
