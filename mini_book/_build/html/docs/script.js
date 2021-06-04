"use strict";
const { useReducer } = React;
const { Button, Progress, Slider } = antd;
const { PlayCircleOutlined, PauseCircleOutlined, UndoOutlined, SoundOutlined, SoundFilled } = icons;
function Player() {
    function init() {
        return {
            plays: false,
            mute: false,
            volume: 1,
            loading: true,
            disabled: true,
            progress: {
                loaded: 0,
                loadedSeconds: 0,
                played: 0,
                playedSeconds: 0
            }
        };
    }
    function reducer(state, { type, payload }) {
        switch (type) {
            case "plays":
                return Object.assign(Object.assign({}, state), { plays: payload });
            case "mute":
                return Object.assign(Object.assign({}, state), { mute: !state.mute });
            case "volume":
                return Object.assign(Object.assign({}, state), { volume: payload });
            case "loading":
                return Object.assign(Object.assign({}, state), { loading: payload });
            case "progress":
                return Object.assign(Object.assign({}, state), { progress: payload });
            case "disabled":
                return Object.assign(Object.assign({}, state), { disabled: payload });
            case "error":
                return Object.assign(Object.assign({}, state), { error: payload });
            case "reset":
                return init();
            default:
                throw new Error("Not found the method or unexpected problem");
        }
    }
    function timeFormat(seconds = 0) {
        return moment(new Date()).startOf("day").seconds(seconds).format("mm:ss");
    }
    const [state, dispatch] = useReducer(reducer, {}, init);
    const size = "small";
    const { plays, volume, mute, loading, disabled, progress } = state;
    return (React.createElement("div", { className: "player" },
        React.createElement(ReactPlayer, { url: "http://www.slspencer.com/Sounds/Star%20Wars/Mouse%20Droid/gen3.wav", playing: plays, loop: false, controls: false, light: false, volume: volume, muted: mute, playbackRate: 1, width: 0, height: 0, style: {}, progressInterval: 1000, playsinline: false, pip: false, stopOnUnmount: true, wrapper: "div",
            // playIcon
            // config
            onReady: () => dispatch({ type: "disabled", payload: false }), onProgress: (played) => dispatch({ type: "progress", payload: played }), onEnded: () => dispatch({ type: "plays", payload: false }), onBuffer: () => dispatch({ type: "loading", payload: true }), onBufferEnd: () => dispatch({ type: "loading", payload: false }), onError: (error) => dispatch({ type: "error", payload: error }) }),
        React.createElement("div", { className: "player__controls" },
            React.createElement(Button, { type: "primary", shape: "circle", icon: React.createElement(UndoOutlined, null), disabled: disabled, size: size }),
            React.createElement(Button, { type: "primary", shape: "circle", icon: plays ? React.createElement(PauseCircleOutlined, null) : React.createElement(PlayCircleOutlined, null), size: size, disabled: disabled, onClick: () => dispatch({ type: "plays", payload: !plays }) })),
        React.createElement(Progress, { percent: progress.played * 100, 
            // showInfo={false}
            size: size, status: loading ? "active" : "normal", format: () => `${timeFormat(progress.playedSeconds)} / ${timeFormat(progress.loadedSeconds)}`, disabled: disabled, onClick: (event) => console.log(event) }),
        React.createElement("div", { className: "player__sound" },
            React.createElement(Button, { type: "primary", shape: "circle", icon: mute ? React.createElement(SoundOutlined, null) : React.createElement(SoundFilled, null), size: size, disabled: disabled, onClick: () => dispatch({ type: "mute", payload: !mute }) }),
            React.createElement(Slider, { disabled: mute || disabled, min: 0, max: 1, step: 0.01, value: volume, onChange: (value) => dispatch({ type: "volume", payload: value }), tooltipVisible: false }))));
}
ReactDOM.render(React.createElement(Player, null), mountNode);

ReactDOM.render(React.createElement(Player, null), mountNode2);

ReactDOM.render(React.createElement(Player, null), mountNode3);