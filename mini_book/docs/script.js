"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var useReducer = React.useReducer;
var Button = antd.Button, Progress = antd.Progress, Slider = antd.Slider;
var PlayCircleOutlined = icons.PlayCircleOutlined, PauseCircleOutlined = icons.PauseCircleOutlined, UndoOutlined = icons.UndoOutlined, SoundOutlined = icons.SoundOutlined, SoundFilled = icons.SoundFilled;
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
    function reducer(state, _a) {
        var type = _a.type, payload = _a.payload;
        switch (type) {
            case "plays":
                return __assign(__assign({}, state), { plays: payload });
            case "mute":
                return __assign(__assign({}, state), { mute: !state.mute });
            case "volume":
                return __assign(__assign({}, state), { volume: payload });
            case "loading":
                return __assign(__assign({}, state), { loading: payload });
            case "progress":
                return __assign(__assign({}, state), { progress: payload });
            case "disabled":
                return __assign(__assign({}, state), { disabled: payload });
            case "error":
                return __assign(__assign({}, state), { error: payload });
            case "reset":
                return init();
            default:
                throw new Error("Not found the method or unexpected problem");
        }
    }
    function timeFormat(seconds) {
        if (seconds === void 0) { seconds = 0; }
        return moment(new Date()).startOf("day").seconds(seconds).format("mm:ss");
    }
    var _a = useReducer(reducer, {}, init), state = _a[0], dispatch = _a[1];
    var size = "small";
    var plays = state.plays, volume = state.volume, mute = state.mute, loading = state.loading, disabled = state.disabled, progress = state.progress;
    return (React.createElement("div", { className: "player" },
        React.createElement(ReactPlayer, { url: "http://www.slspencer.com/Sounds/Star%20Wars/Mouse%20Droid/gen3.wav", playing: plays, loop: false, controls: false, light: false, volume: volume, muted: mute, playbackRate: 1, width: 0, height: 0, style: {}, progressInterval: 1000, playsinline: false, pip: false, stopOnUnmount: true, wrapper: "div", 
            // playIcon
            // config
            onReady: function () { return dispatch({ type: "disabled", payload: false }); }, onProgress: function (played) { return dispatch({ type: "progress", payload: played }); }, onEnded: function () { return dispatch({ type: "plays", payload: false }); }, onBuffer: function () { return dispatch({ type: "loading", payload: true }); }, onBufferEnd: function () { return dispatch({ type: "loading", payload: false }); }, onError: function (error) { return dispatch({ type: "error", payload: error }); } }),
        React.createElement("div", { className: "player__controls" },
            React.createElement(Button, { type: "primary", shape: "circle", icon: React.createElement(UndoOutlined, null), disabled: disabled, size: size }),
            React.createElement(Button, { type: "primary", shape: "circle", icon: plays ? React.createElement(PauseCircleOutlined, null) : React.createElement(PlayCircleOutlined, null), size: size, disabled: disabled, onClick: function () { return dispatch({ type: "plays", payload: !plays }); } })),
        React.createElement(Progress, { percent: progress.played * 100, 
            // showInfo={false}
            size: size, status: loading ? "active" : "normal", format: function () {
                return timeFormat(progress.playedSeconds) + " / " + timeFormat(progress.loadedSeconds);
            }, disabled: disabled, onClick: function (event) { return console.log(event); } }),
        React.createElement("div", { className: "player__sound" },
            React.createElement(Button, { type: "primary", shape: "circle", icon: mute ? React.createElement(SoundOutlined, null) : React.createElement(SoundFilled, null), size: size, disabled: disabled, onClick: function () { return dispatch({ type: "mute", payload: !mute }); } }),
            React.createElement(Slider, { disabled: mute || disabled, min: 0, max: 1, step: 0.01, value: volume, onChange: function (value) { return dispatch({ type: "volume", payload: value }); }, tooltipVisible: false }))));
}
ReactDOM.render(React.createElement(Player, null), mountNode);