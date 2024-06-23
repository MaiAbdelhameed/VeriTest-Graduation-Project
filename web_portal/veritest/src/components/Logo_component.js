import Image from "next/image";
export default function Logo() {
  return (
    <div className="row  ">
      {/* website logo div */}
      <div className="col d-flex align-items-center justify-content-center">
        <Image src="/veritest.png" width={500} height={375} />
      </div>
    </div>
  );
}
