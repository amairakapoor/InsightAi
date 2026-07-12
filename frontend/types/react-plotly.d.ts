declare module "react-plotly.js" {
  import { Component } from "react";
  interface PlotParams {
    data: any[];
    layout?: any;
    config?: any;
    style?: React.CSSProperties;
    useResizeHandler?: boolean;
    className?: string;
  }
  export default class Plot extends Component<PlotParams> {}
}
